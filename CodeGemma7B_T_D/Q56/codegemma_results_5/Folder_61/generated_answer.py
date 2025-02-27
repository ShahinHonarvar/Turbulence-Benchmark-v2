from itertools import permutations

def all_substring_of_size_n(s):

    def check(x):
        return len(x) == 39 and len(set(x)) == 39
    a = [''.join(i) for i in permutations(s, 39) if check(i)]
    return a if a else []