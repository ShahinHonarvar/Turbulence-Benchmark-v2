def all_substring_of_size_n(s):
    all_substr = []
    for i in range(len(s) - 55):
        substring = s[i:i + 56]
        all_substr.append(sanitize(substring))
    return list(set(all_substr))

def sanitize(substring):
    return ''.join(sorted(set(substring)))