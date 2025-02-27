def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagrams_count = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) < 3 or len(strings[j]) < 3:
                continue
            sorted_i = sort_string(strings[i])
            sorted_j = sort_string(strings[j])
            if sorted_i == sorted_j:
                pair = (min(strings[i].lower(), strings[j].lower()), max(strings[i].lower(), strings[j].lower()))
                if pair not in checked_pairs:
                    checked_pairs.add(pair)
                    anagrams_count += 1
                    if anagrams_count >= 17:
                        return True
    return False