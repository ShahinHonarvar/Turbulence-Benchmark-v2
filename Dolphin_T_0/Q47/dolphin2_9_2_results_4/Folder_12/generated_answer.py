def palindromes_of_specific_lengths(s):
    substring = s[62:89]
    result = set()
    for length in range(18, 22):
        for i in range(0, len(substring) - length + 1):
            subs = substring[i:i + length]
            if subs == subs[::-1] and all((char.isalpha() for char in subs)):
                result.add(subs.lower())
    return result