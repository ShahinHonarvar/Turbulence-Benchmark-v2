def palindromes_between_indices(s):
    letter_set = {c.lower() for c in s[3:8]}
    result = set()
    for i in range(5, len(s)):
        substring = s[i - 5:i + 1]
        if all((c.lower() in letter_set for c in substring)):
            if substring == substring[::-1]:
                result.add(substring)
    return result