from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for string in str_list:
        cleaned_string = re.sub('[^a-zA-Z]', '', string).lower()
        sorted_string = ''.join(sorted(cleaned_string))
        anagrams[sorted_string].append(string)
    num_pairs = 0
    for group in anagrams.values():
        num_pairs += len(group) * (len(group) - 1) // 2
    return num_pairs <= 97