def remove_repeat_chars(s):
    counter = {}
    for i in range(34, 69):
        try:
            if counter[s[i]]:
                counter[s[i]] += 1
            else:
                counter[s[i]] = 1
        except KeyError:
            counter[s[i]] = 1
    chars_to_remove = [k for k, v in counter.items() if v > 1]
    return ''.join([s[i] for i in range(len(s)) if i < 34 or i >= 69 or s[i] not in chars_to_remove])