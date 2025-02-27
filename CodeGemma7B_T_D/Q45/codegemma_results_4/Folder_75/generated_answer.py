def palindromes_between_indices(string):
    if 2 < len(string) < 5:
        return set()
    for i in range(ord('a'), ord('z') + 1):
        for j in range(ord('a'), ord('z') + 1):
            for k in range(ord('a'), ord('z') + 1):
                if string[2:5] == chr(i) + chr(j) + chr(k):
                    tmp = ''.join(sorted([chr(i) + chr(j) + chr(k)]))[::-1]
                    if tmp.lower() == string[2:5].lower():
                        return set([tmp])