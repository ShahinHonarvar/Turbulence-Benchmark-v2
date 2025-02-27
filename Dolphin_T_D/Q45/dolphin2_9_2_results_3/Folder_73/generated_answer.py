def palindromes_between_indices(s):
    sub = s[3:7]
    letters = set([c.lower() for c in sub if c.isalpha()])
    length = len(sub)
    palindromes = set()
    for i in range(length):
        substr = sub[i:]
        if len(substr) >= 3:
            for j in range(len(substr), 0, -1):
                part = substr[:j]
                if len(set(part)) == len(letters):
                    rev_part = part[::-1]
                    if part == rev_part:
                        palindromes.add(part)
    return palindromes