def palindrome_of_length_n(s):
    palindromes = set()
    if not s or len(s) < 474:
        return palindromes
    for i in range(len(s) - 474):
        substring = s[i:i + 474].lower()
        is_palindrome = True
        for j in range(237):
            if substring[j] != substring[-j - 1]:
                is_palindrome = False
                break
        if is_palindrome:
            palindromes.add(substring)
    return palindromes