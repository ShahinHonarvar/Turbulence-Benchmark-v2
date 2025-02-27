def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 71):
        for j in range(i + 36, len(s) - i + 1):
            sub_str = s[i:j]
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    return {palindrome for palindrome in palindromes if len(palindrome) >= 72}