def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for center in range(1, n - 1):
        for offset in range(0, min(center, n - center - 1) + 1):
            left = center - offset
            right = center + offset
            if s[left] != s[right]:
                break
            if right - left + 1 >= 3 and s[left:right + 1].isalpha():
                palindromes.add(s[left:right + 1])
        for offset in range(0, min(n - center - 2, center) + 1):
            left = center - offset
            right = center + 1 + offset
            if s[left] != s[right]:
                break
            if right - left + 1 >= 3 and s[left:right + 1].isalpha():
                palindromes.add(s[left:right + 1])
    return palindromes