def palindromes_of_specific_lengths(s):
    s = s[45:99]
    s = ''.join(filter(str.isalpha, s)).lower()
    found_palindromes = set()
    for length in range(40, 48):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                found_palindromes.add(substring)
    return found_palindromes