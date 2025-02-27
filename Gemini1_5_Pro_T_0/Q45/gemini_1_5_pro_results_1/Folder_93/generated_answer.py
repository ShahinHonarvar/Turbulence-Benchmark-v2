def palindromes_between_indices(text):
    s = set()
    for i in range(2, 8):
        for j in range(i, 8):
            temp = text[2:i] + text[i:j + 1]
            if len(temp) >= 6:
                for k in range(len(temp) // 2):
                    if temp[k].lower() != temp[len(temp) - 1 - k].lower():
                        break
                else:
                    permutations = set((''.join(p) for p in itertools.permutations(temp)))
                    for permutation in permutations:
                        l = len(permutation)
                        for m in range(l // 2):
                            if permutation[m].lower() != permutation[l - 1 - m].lower():
                                break
                        else:
                            s.add(permutation)
    return s