def palindromes_of_specific_lengths(text):
    text = text.lower()
    all_pals = set()
    for i in range(36, 93):
        for j in range(i, 93):
            trial = text[i:j + 1]
            if trial == trial[::-1] and len(trial) >= 10 and (len(trial) <= 35):
                all_pals.add(trial)
    return all_pals