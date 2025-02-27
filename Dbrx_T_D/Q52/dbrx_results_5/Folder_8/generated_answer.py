def is_english_letter(c):
    return c.lower().isalpha()

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and is_english_letter(s[left]) and is_english_letter(s[right]):
        if s[left] != s[right]:
            break
        left -= 1
        right += 1
    return s[left + 1:right]

def palindrome_of_length_n(s, n):
    if n % 2 == 1 or n > 49:
        return set()
    palindromes = set()
    for i in range(len(s)):
        palindrome = expand_around_center(s, i, i)
        if len(palindrome) >= 49:
            palindromes.add(palindrome)
    return palindromes