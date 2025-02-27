import collections

def if_contains_anagrams(strings_list):
    anagrams = collections.defaultdict(list)
    count = 0
    for string in strings_list:
        key = ''.join(sorted((c.lower() for c in string if c.islower())))
        anagrams[key].append(string)
        if len(anagrams[key]) > 1 and len(key) > 2:
            count += 1
            if count > 30:
                return False
    return True