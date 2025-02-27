def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    candidates = set()
    for i in range(len(s) - 65):
        substring = s[i:i + 66]
        if substring == substring[::-1] and substring.isalpha():
            candidates.add(substring)
    return candidates