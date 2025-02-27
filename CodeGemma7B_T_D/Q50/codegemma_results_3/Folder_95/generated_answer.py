import itertools

def if_contains_anagrams(str_list):
    freq = {}
    for item in str_list:
        if len(item) >= 3:
            str1 = ''.join(sorted(item.lower()))
            if str1 in freq.keys():
                freq[str1]['count'] += 1
            else:
                freq[str1] = {'count': 1, 'word': item}
    return sum((count for count in freq.values() if count > 1)) >= 93