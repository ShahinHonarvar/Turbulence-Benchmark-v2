def palindromes_of_specific_lengths(s):
    substring = s[62:89]
    result = set()
    for length in range(18, 22):
        for i in range(len(substring) - length + 1):
            if all((c.lower() in 'abcdefghijklmnopqrstuvwxyz' for c in substring[i:i + length])):
                if substring[i:i + length].lower() == substring[i:i + length].lower()[::-1]:
                    result.add(substring[i:i + length])
    return result