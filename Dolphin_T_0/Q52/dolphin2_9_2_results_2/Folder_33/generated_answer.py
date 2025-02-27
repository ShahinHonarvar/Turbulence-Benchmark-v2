def palindrome_of_length_n(s):
    s = s.lower()
    all_palindromes = set()
    length = 475
    for i in range(len(s) - length + 1):
        sub = s[i:i + length]
        if sub == sub[::-1] and sub.isalpha():
            all_palindromes.add(sub)
    return all_palindromes