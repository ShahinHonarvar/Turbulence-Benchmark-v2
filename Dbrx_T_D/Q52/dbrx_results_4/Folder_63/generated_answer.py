def palindrome_of_length_n(s: str) -> set:
    n = 18
    if len(s) < n:
        return set()
    palindrome_set = set()
    for i in range(len(s) - n + 1):
        s_sub = s[i:i + n]
        if s_sub.lower() == s_sub[::-1].lower():
            palindrome_set.add(s_sub)
    return palindrome_set