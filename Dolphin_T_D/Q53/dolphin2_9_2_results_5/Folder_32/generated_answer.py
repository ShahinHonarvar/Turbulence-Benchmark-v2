def palindrome_of_length_at_least_n(s):
    set_of_palindromes = set()
    for i in range(len(s)):
        for j in range(i + 69, len(s)):
            if s[i].lower() == s[j].lower():
                if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1].isalpha():
                    set_of_palindromes.add(s[i:j + 1])
    return set_of_palindromes