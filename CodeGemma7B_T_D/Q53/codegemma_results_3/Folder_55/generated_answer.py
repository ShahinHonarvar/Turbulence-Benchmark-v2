from collections import defaultdict

def palindrome_of_length_at_least_n(seq):
    cnt = defaultdict(int)
    for x in seq:
        cnt[x.lower()] += 1
    maxlen = 0
    ans = set()
    for c, freq in cnt.items():
        if freq >= maxlen:
            maxlen = freq
            ans.add(c * freq)
    return ans