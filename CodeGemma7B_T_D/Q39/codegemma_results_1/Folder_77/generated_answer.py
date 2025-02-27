from functools import cmp_to_key

def return_n_greatest_chars(string):

    def compare_chars(char1, char2):
        return ord(char1) - ord(char2)
    sorted_chars = sorted(string, key=cmp_to_key(compare_chars), reverse=True)[:47]
    return sorted_chars