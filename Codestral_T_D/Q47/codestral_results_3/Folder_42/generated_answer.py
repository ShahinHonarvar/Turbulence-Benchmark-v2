def palindromes_of_specific_lengths(text):
    sub_text = text[43:96].lower()
    palindromes = set()
    for length in range(18, 48):
        for i in range(len(sub_text) - length + 1):
            sub_str = sub_text[i:i + length]
            if sub_str == sub_str[::-1] and sub_str.isalpha():
                palindromes.add(sub_str)
    return palindromes