def palindrome_of_length_at_least_n(s):
    string_lower = s.lower()
    palindromes_set = set()
    for i in range(len(string_lower)):
        for j in range(i + 7, len(string_lower)):
            substring = string_lower[i:j + 1]
            if substring == substring[::-1]:
                palindromes_set.add(substring)
    return palindromes_set