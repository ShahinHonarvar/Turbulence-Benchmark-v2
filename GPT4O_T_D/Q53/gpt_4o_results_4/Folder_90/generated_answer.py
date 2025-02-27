def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    length = len(s)
    found_palindromes = set()
    for i in range(length):
        for j in range(i + 140, length + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                found_palindromes.add(substring)
    return found_palindromes