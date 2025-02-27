def palindromes_of_specific_lengths(text):
    sub_text = text[35:88]
    palindromes = set()
    for length in range(24, 34):
        for i in range(0, len(sub_text) - length + 1):
            sub = sub_text[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes