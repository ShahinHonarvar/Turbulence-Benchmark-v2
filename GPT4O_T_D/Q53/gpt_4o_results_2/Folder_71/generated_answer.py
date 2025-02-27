def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    found_palindromes = set()
    for i in range(len(s)):
        for j in range(i + 87, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                found_palindromes.add(substring)
    return found_palindromes