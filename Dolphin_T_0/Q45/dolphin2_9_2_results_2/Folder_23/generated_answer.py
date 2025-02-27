def palindromes_between_indices(s):
    letters = set(s[0:7].lower())
    if not letters:
        return set()
    return set(letters | {''.join(letters)[i:i + 4] for i in range(len(''.join(letters)) - 3) if ''.join(letters)[i:i + 4] == ''.join(letters)[i:i + 4][::-1]})