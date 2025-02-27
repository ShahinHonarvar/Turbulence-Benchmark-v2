def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(15, 90):
        for length in range(40, 73):
            if i + length > 90:
                break
            substring = s[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes