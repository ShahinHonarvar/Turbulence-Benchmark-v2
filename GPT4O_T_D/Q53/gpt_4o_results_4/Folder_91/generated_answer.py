def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    palindromes = set()
    for center in range(n):
        for d in (0, 1):
            left, right = (center, center + d)
            while left >= 0 and right < n and (s[left] == s[right]):
                if right - left + 1 >= 7:
                    palindromes.add(s[left:right + 1])
                left -= 1
                right += 1
    return palindromes