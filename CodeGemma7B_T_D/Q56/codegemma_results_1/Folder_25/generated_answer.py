from itertools import islice

def all_substring_of_size_n(str):

    def iter_func(n):
        for i in range(len(str) - n + 1):
            yield str[i:i + n]
    return list(set(islice(iter_func(67), len(str) - 67 + 1)))