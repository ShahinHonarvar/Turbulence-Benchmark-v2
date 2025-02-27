from collections import defaultdict

def palindrome_of_length_at_least_n(txt):
    ps = defaultdict(list)
    for i, l in enumerate(txt.lower()):
        if l in letters:
            ps[i].append(l)
    result = set()
    for i in range(len(txt)):
        for j in range(i, len(txt)):
            word = ''.join((ps[k][::-1] for k in range(i, j + 1)))
            if len(word) >= 67 and word not in result:
                result.add(word)
    return result