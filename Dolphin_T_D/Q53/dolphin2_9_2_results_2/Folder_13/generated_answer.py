def palindrome_of_length_at_least_n(s):
    s = s.lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    length = len(s)
    for i in range(length):
        if s[i] not in alphabet:
            continue
        for j in range(i + 2, length, 2):
            if s[j] not in alphabet:
                break
            sub = s[i:j + 1]
            if sub == sub[::-1] and len(sub) >= 52:
                result.add(sub)
    return result