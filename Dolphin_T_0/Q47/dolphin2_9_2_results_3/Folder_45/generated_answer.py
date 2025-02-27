def palindromes_of_specific_lengths(text):
    palindromes = set()
    relevant_text = text[70:141]
    for length in range(3, 61):
        for i in range(len(relevant_text) - length + 1):
            substring = relevant_text[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes