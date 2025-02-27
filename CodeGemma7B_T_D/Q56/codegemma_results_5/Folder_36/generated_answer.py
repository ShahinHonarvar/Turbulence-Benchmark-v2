from collections import defaultdict

def all_substring_of_size_n(str):
    result, charset = ([], defaultdict(int))
    for i in range(len(str)):
        if i >= n - 1:
            if len(charset) == n:
                result.append(''.join(sorted(charset.elements())))
            charset[str[i - (n - 1)]] -= 1
            if charset[str[i - (n - 1)]] == 0:
                charset.pop(str[i - (n - 1)])
        charset[str[i]] += 1
    return result