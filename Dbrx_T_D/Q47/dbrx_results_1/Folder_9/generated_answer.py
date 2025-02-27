def palindromes_of_specific_lengths(text):
    palindromes = set()
    for length in range(50, 61):
        for i in range(301 - length):
            if text[i:i + length].isalpha() and text[i:i + length].lower() == text[i:i + length][::-1].lower():
                palindromes.add(text[i:i + length])
    return palindromes