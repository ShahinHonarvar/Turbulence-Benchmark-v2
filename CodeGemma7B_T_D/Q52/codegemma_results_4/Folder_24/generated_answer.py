from collections import defaultdict
from string import ascii_lowercase

def palindrome_of_length_n(s):

    def first_palindrome(first, middle):
        f2p = defaultdict(set)
        flag = defaultdict(int)
        for i in middle:
            new_letters = first + i + first[::-1]
            for j in new_letters:
                if j in flag:
                    flag[j] = 1
                else:
                    flag[j] = 0
                if flag[j] == 2:
                    f2p[j].add(i)
                    flag[j] = 0
        return f2p
    f2p = defaultdict(set)
    for letter in ascii_lowercase:
        f2p[letter] = {letter}
    for i in range(len(s)):
        first_palindrome(s[i], s[i + 1:])
    if f2p.values():
        return {''.join(p) for p in f2p.values()}
    else:
        return set()