def all_substring_of_size_n(test_str):
    unique_subs = set()
    n = 99
    for i in range(len(test_str) - n + 1):
        substring = test_str[i:i + n]
        unique_subs.add(substring)
    return list(unique_subs)