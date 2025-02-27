def distinct_substrings(input_str, n):
    substrs = set()
    for i in range(0, len(input_str) - n + 1):
        sub = input_str[i:i + n]
        substrs.add(sub)
    return list(substrs)

def all_substring_of_size_n(input_str):
    substrs = distinct_substrings(input_str, 105)
    return [s for s in substrs if len(set(s)) == len(s)]