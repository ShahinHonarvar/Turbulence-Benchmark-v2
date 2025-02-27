def palindromes_between_indices(s):
    create_set = set()
    s = ''.join(sorted(s.lower()))
    for i in range(3, len(s) + 1):
        for j in range(len(s) - i + 1):
            sub = s[j:j + i]
            if sub == sub[::-1]:
                create_set.add(sub)
    return create_set