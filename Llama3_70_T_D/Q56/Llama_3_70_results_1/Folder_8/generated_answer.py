def all_substring_of_size_n(s):
    return [s[i:i + 30] for i in range(len(s) - 29) if len(set(s[i:i + 30])) == 30 and s[i:i + 30] not in [s[j:j + 30] for j in range(i)]] if len(s) >= 30 else []