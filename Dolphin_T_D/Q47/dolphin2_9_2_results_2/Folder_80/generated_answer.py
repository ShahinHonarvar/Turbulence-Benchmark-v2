def palindromes_of_specific_lengths(s):
    sub_string = s[35:89]
    palindromes = set()
    for length in range(24, 34):
        for i in range(len(sub_string) - length + 1):
            if sub_string[i:i + length].lower() == sub_string[i:i + length].lower()[::-1] and sub_string[i:i + length].lower().isalpha():
                palindromes.add(sub_string[i:i + length])
    return palindromes