def remove_repeat_chars(s):
    repeated = set()
    for i in range(90, 200):
        if s[i] not in repeated:
            for j in range(i + 1, 200):
                if s[j] == s[i]:
                    repeated.add(s[j])
    return ''.join([c for c in s if c not in repeated])