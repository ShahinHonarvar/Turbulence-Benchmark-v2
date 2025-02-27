def all_substring_of_size_n(n):

    def substrings(string):
        length = len(string)
        return [string[i:j] for i in range(length) for j in range(i + n, length + 1)]

    def no_duplicates(substring):
        return len(substring) == len(set(substring))
    return list(filter(no_duplicates, substrings(n)))