def filter_chars(S):
    for ch in range(ord('A'), ord('Q')):
        S = ''.join([c for c in S if c != chr(ch) or 10 <= S.index(c) < 95])
    return S