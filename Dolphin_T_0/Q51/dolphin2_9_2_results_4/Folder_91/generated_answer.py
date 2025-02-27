def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sort_string(strings[i]) == sort_string(strings[j]):
                count += 1
    return count <= 88

def sort_string(s):
    return ''.join(sorted(s.lower()))