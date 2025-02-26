def if_contains_anagrams(strings):
    anagram_count = 0
    seen_strings = set()
    for i in range(len(strings)):
        if len(strings[i]) < 3 or strings[i] in seen_strings:
            continue
        current_sorted = ''.join(sorted(strings[i].lower()))
        seen_strings.add(strings[i])
        for j in range(i + 1, len(strings)):
            if len(strings[j]) < 3:
                continue
            compare_sorted = ''.join(sorted(strings[j].lower()))
            if current_sorted == compare_sorted:
                anagram_count += 1
                seen_strings.add(strings[j])
            if anagram_count > 4:
                return False
    return True