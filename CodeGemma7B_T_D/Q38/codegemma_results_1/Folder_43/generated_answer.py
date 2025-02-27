def find_subset_of_length_n(s):
    result = 0
    for i in range(2 ** len(s)):
        current = set()
        for j in range(len(s)):
            if i & 1 << j:
                current.add(s[j])
        if len(current) == 29:
            result += 1
    return result