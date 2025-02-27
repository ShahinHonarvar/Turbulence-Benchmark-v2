from functools import reduce

def find_original_set(set_a, set_b, set_c, set_d, set_e, set_f, set_g, set_h, set_i, set_j, set_k, set_l, set_m, set_n, set_o, set_p, set_q, set_r, set_s, set_t, set_u, set_v, set_w, set_x, set_y, set_z, set_aa, set_ab, set_ac, set_ad, set_ae, set_af, set_ag, set_ah, set_ai, set_aj, set_ak, set_al, set_am, set_an, set_ao, set_ap, set_aq, set_ar, set_as, set_at, set_au, set_av, set_aw, set_ax, set_ay, set_az):
    list_of_sets = [set_a, set_b, set_c, set_d, set_e, set_f, set_g, set_h, set_i, set_j, set_k, set_l, set_m, set_n, set_o, set_p, set_q, set_r, set_s, set_t, set_u, set_v, set_w, set_x, set_y, set_z, set_aa, set_ab, set_ac, set_ad, set_ae, set_af, set_ag, set_ah, set_ai, set_aj, set_ak, set_al, set_am, set_an, set_ao, set_ap, set_aq, set_ar, set_as, set_at, set_au, set_av, set_aw, set_ax, set_ay, set_az]
    original_set = reduce(lambda original, s: original if original.issuperset(s) else s, list_of_sets)
    return original_set