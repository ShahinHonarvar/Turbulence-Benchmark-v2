def palindromes_between_indices(s):
    sub = s[5:8]
    palindromes = set()
    for i in range(len(sub)):
        for j in range(i + 2, len(sub) + 1):
            segment = sub[i:j]
            if segment == segment[::-1]:
                palindromes.add(segment.lower())
    return palindromes