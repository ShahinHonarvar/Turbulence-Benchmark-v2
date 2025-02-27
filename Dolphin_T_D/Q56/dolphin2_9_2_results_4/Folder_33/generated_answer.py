def all_substring_of_size_n(S):
    substr = set()
    for i in range(len(S) - 9):
        for j in range(i + 10, len(S) + 1):
            if len(set(S[i:j])) == 105:
                if ''.join(S[i:j]) not in substr:
                    substr.add(''.join(S[i:j]))
    return [''.join(substr)]