def palindromes_between_indices(s):
    substring = s[6:9]
    letters = [ch for ch in substring.lower() if ch.isalpha()]
    if len(set(letters)) < 4:
        return set()
    subs = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            sub = ''.join(letters[i:j])
            if len(sub) >= 4 and sub == sub[::-1]:
                subs.add(sub)
    return subs